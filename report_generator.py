import os
import shutil

import matplotlib.pyplot as plt
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer


class ReportGenerator:
    """
    Esta es la clase ReportGenerator que se utiliza para generar informes de simulación.

    Atributos:
        logs (list): Los registros de la simulación.
        results_dir (str): El directorio en el que se guardan los resultados de la simulación.
        time_series (list): La serie de tiempo de la simulación.
        total_utility_series (list): La serie de utilidad total de la simulación.
        total_traffic_series (list): La serie de tráfico total de la simulación.
        node_utility_series (dict): Las series de utilidad de los nodos de la simulación.
        instance_utility_series (dict): Las series de utilidad de las instancias de la simulación.
        node_traffic_series (dict): Las series de tráfico de los nodos de la simulación.
        instance_traffic_series (dict): Las series de tráfico de las instancias de la simulación.
        node_resources_series (dict): Las series de recursos de los nodos de la simulación.
        instance_resources_series (dict): Las series de recursos de las instancias de la simulación.
    """

    def __init__(self, logs, results_dir="results"):
        self.logs = logs
        self.results_dir = results_dir
        self.time_series = []
        self.total_utility_series = []
        self.total_traffic_series = []
        self.node_utility_series = {}
        self.instance_utility_series = {}
        self.node_traffic_series = {}
        self.instance_traffic_series = {}
        self.node_resources_series = {}
        self.instance_resources_series = {}

        if os.path.exists(self.results_dir):
            shutil.rmtree(self.results_dir)
        os.makedirs(self.results_dir)

    def process_logs(self):
        for log in self.logs:
            time = log['time']
            total_utility = 0
            total_traffic = 0

            for node in log['nodes']:
                node_name = node['name']
                if node_name not in self.node_utility_series:
                    self.node_utility_series[node_name] = []
                    self.node_traffic_series[node_name] = []
                    self.node_resources_series[node_name] = {'CPU': [], 'RAM': [], 'STORAGE': []}

                node_utility = 0
                node_traffic = 0
                for resource, value in node['resources'].items():
                    self.node_resources_series[node_name][resource].append(value)

                for instance in node['instances']:
                    instance_name = instance['name']
                    if instance_name not in self.instance_utility_series:
                        self.instance_utility_series[instance_name] = []
                        self.instance_traffic_series[instance_name] = []
                        self.instance_resources_series[instance_name] = {'CPU': [], 'RAM': [], 'STORAGE': []}

                    utility = instance['utility']
                    traffic = instance['traffic']
                    self.instance_utility_series[instance_name].append(utility)
                    self.instance_traffic_series[instance_name].append(traffic)
                    self.instance_resources_series[instance_name]['CPU'].append(instance['cpu_request'])
                    self.instance_resources_series[instance_name]['RAM'].append(instance['ram_request'])
                    self.instance_resources_series[instance_name]['STORAGE'].append(instance['storage_request'])

                    node_utility += utility
                    node_traffic += traffic

                self.node_utility_series[node_name].append(node_utility)
                self.node_traffic_series[node_name].append(node_traffic)

                total_utility += node_utility
                total_traffic += node_traffic

            self.time_series.append(time)
            self.total_utility_series.append(total_utility)
            self.total_traffic_series.append(total_traffic)

    def save_plot(self, df, x_col, y_col, title, x_label, y_label, filename):
        plt.figure(figsize=(10, 6))
        plt.plot(df[x_col], df[y_col], marker='o')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid(True)
        plt.savefig(os.path.join(self.results_dir, filename))
        plt.close()

    def save_series_plot(self, series_dict, title, x_label, y_label, filename):
        plt.figure(figsize=(10, 6))
        for name, series in series_dict.items():
            plt.plot(self.time_series, series, marker='o', label=name)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(self.results_dir, filename))
        plt.close()

    def generate_plots(self):
        df_total_utility = pd.DataFrame({'Time': self.time_series, 'Total Utility': self.total_utility_series})
        df_total_traffic = pd.DataFrame({'Time': self.time_series, 'Total Traffic': self.total_traffic_series})

        self.save_plot(df_total_utility, 'Time', 'Total Utility', 'Utilidad Total durante la Simulación', 'Tiempo',
                       'Utilidad Total', 'total_utility.png')
        self.save_plot(df_total_traffic, 'Time', 'Total Traffic', 'Tráfico Total durante la Simulación', 'Tiempo',
                       'Tráfico Total', 'total_traffic.png')

        self.save_series_plot(self.node_utility_series, 'Utilidad por Nodo', 'Tiempo', 'Utilidad', 'node_utility.png')
        self.save_series_plot(self.instance_utility_series, 'Utilidad por Instancia', 'Tiempo', 'Utilidad',
                              'instance_utility.png')
        self.save_series_plot(self.node_traffic_series, 'Tráfico por Nodo', 'Tiempo', 'Tráfico', 'node_traffic.png')
        self.save_series_plot(self.instance_traffic_series, 'Tráfico por Instancia', 'Tiempo', 'Tráfico',
                              'instance_traffic.png')

        for resource_type in ['CPU', 'RAM', 'STORAGE']:
            self.save_series_plot(
                {name: series[resource_type] for name, series in self.node_resources_series.items()},
                f'Cambios en {resource_type} en Nodos',
                'Tiempo',
                f'{resource_type} Disponible',
                f'node_{resource_type.lower()}.png'
            )
            self.save_series_plot(
                {name: series[resource_type] for name, series in self.instance_resources_series.items()},
                f'Cambios en {resource_type} en Instancias',
                'Tiempo',
                f'{resource_type} Solicitado',
                f'instance_{resource_type.lower()}.png'
            )

    def add_table_to_pdf(self, elements, data, title):
        styles = getSampleStyleSheet()
        elements.append(Paragraph(title, styles['Heading2']))
        elements.append(Spacer(1, 12))  # Añadir espacio entre título y tabla
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 12))  # Añadir espacio entre tablas

    def add_image_to_pdf(self, elements, image_path, title):
        styles = getSampleStyleSheet()
        elements.append(Paragraph(title, styles['Heading2']))
        elements.append(Spacer(1, 12))  # Añadir espacio entre título y gráfico
        elements.append(Image(image_path, width=500, height=300))
        elements.append(Spacer(1, 12))  # Añadir espacio entre gráficos

    def generate_pdf(self):
        pdf_path = os.path.join(self.results_dir, "simulation_report.pdf")
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)
        elements = []
        styles = getSampleStyleSheet()

        elements.append(Paragraph("Reporte de Simulación", styles['Title']))
        elements.append(Spacer(1, 12))  # Añadir espacio entre título y primer contenido

        images = [
            ('total_utility.png', 'Utilidad Total durante la Simulación'),
            ('total_traffic.png', 'Tráfico Total durante la Simulación'),
            ('node_utility.png', 'Utilidad por Nodo'),
            ('instance_utility.png', 'Utilidad por Instancia'),
            ('node_traffic.png', 'Tráfico por Nodo'),
            ('instance_traffic.png', 'Tráfico por Instancia')
        ]

        for resource_type in ['CPU', 'RAM', 'STORAGE']:
            images.append((f'node_{resource_type.lower()}.png', f'Cambios en {resource_type} en Nodos'))
            images.append((f'instance_{resource_type.lower()}.png', f'Cambios en {resource_type} en Instancias'))

        for image, title in images:
            self.add_image_to_pdf(elements, os.path.join(self.results_dir, image), title)

        for instance_name, utility_series in self.instance_utility_series.items():
            traffic_series = self.instance_traffic_series[instance_name]
            cpu_series = self.instance_resources_series[instance_name]['CPU']
            ram_series = self.instance_resources_series[instance_name]['RAM']
            storage_series = self.instance_resources_series[instance_name]['STORAGE']

            data = [['Tiempo', 'Utilidad', 'Tráfico', 'CPU Solicitado', 'RAM Solicitado', 'STORAGE Solicitado']]
            for i in range(len(self.time_series)):
                data.append([
                    self.time_series[i],
                    utility_series[i],
                    traffic_series[i],
                    cpu_series[i],
                    ram_series[i],
                    storage_series[i]
                ])
            self.add_table_to_pdf(elements, data, f'Datos de {instance_name}')

        doc.build(elements)
