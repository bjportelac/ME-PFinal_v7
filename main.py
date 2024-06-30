from cluster import Cluster
from node import Node
from pod import Pod
from scheduler import Scheduler
from simulation import Simulation


def main():
    # Crear el cluster y los nodos
    cluster = Cluster()
    node1 = Node('Node1')
    node2 = Node('Node2')
    node3 = Node('Node3')
    cluster.add_node(node1)
    cluster.add_node(node2)
    cluster.add_node(node3)

    # Crear instancias (pods)
    instance1 = Pod('Instance1', 50, 100, 200)
    instance2 = Pod('Instance2', 30, 50, 100)
    instance3 = Pod('Instance3', 20, 80, 150)
    instance4 = Pod('Instance4', 32, 64, 500)
    instance5 = Pod('Instance5', 16, 32, 200)

    # Asignar instancias usando el Scheduler
    scheduler = Scheduler()
    for instance in [instance1, instance2, instance3, instance4, instance5]:
        node = scheduler.first_fit(cluster, instance)
        if node:
            print(f'Instance {instance.name} assigned to {node.name}')
        else:
            print(f'No node could accommodate instance {instance.name}')

    # Configurar y ejecutar la simulación
    simulation = Simulation(cluster, duration=50)  # Simula por 1000 segundos virtuales
    simulation.run()

    # Obtener los logs de la simulación
    logs = simulation.logger.get_logs()

    # Ejemplo de análisis de logs (imprimir algunos logs)
    #for log in logs[:5]:  # Mostrar los primeros 5 logs
    #    print(log)

    import os
    import shutil
    import matplotlib.pyplot as plt
    import pandas as pd
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer

    # Directorio de resultados
    results_dir = "results"

    # Crear o limpiar el directorio de resultados
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    os.makedirs(results_dir)

    # Procesar los logs
    time_series = []
    total_utility_series = []
    total_traffic_series = []
    node_utility_series = {}
    instance_utility_series = {}
    node_traffic_series = {}
    instance_traffic_series = {}
    node_resources_series = {}
    instance_resources_series = {}

    for log in logs:
        time = log['time']
        total_utility = 0
        total_traffic = 0

        for node in log['nodes']:
            node_name = node['name']
            if node_name not in node_utility_series:
                node_utility_series[node_name] = []
                node_traffic_series[node_name] = []
                node_resources_series[node_name] = {'CPU': [], 'RAM': [], 'STORAGE': []}

            node_utility = 0
            node_traffic = 0
            for resource, value in node['resources'].items():
                node_resources_series[node_name][resource].append(value)

            for instance in node['instances']:
                instance_name = instance['name']
                if instance_name not in instance_utility_series:
                    instance_utility_series[instance_name] = []
                    instance_traffic_series[instance_name] = []
                    instance_resources_series[instance_name] = {'CPU': [], 'RAM': [], 'STORAGE': []}

                utility = instance['utility']
                traffic = instance['traffic']
                instance_utility_series[instance_name].append(utility)
                instance_traffic_series[instance_name].append(traffic)
                instance_resources_series[instance_name]['CPU'].append(instance['cpu_request'])
                instance_resources_series[instance_name]['RAM'].append(instance['ram_request'])
                instance_resources_series[instance_name]['STORAGE'].append(instance['storage_request'])

                node_utility += utility
                node_traffic += traffic

            node_utility_series[node_name].append(node_utility)
            node_traffic_series[node_name].append(node_traffic)

            total_utility += node_utility
            total_traffic += node_traffic

        time_series.append(time)
        total_utility_series.append(total_utility)
        total_traffic_series.append(total_traffic)

    # Crear DataFrames para graficar
    df_total_utility = pd.DataFrame({'Time': time_series, 'Total Utility': total_utility_series})
    df_total_traffic = pd.DataFrame({'Time': time_series, 'Total Traffic': total_traffic_series})

    # Función para guardar gráficos
    def save_plot(df, x_col, y_col, title, x_label, y_label, filename):
        plt.figure(figsize=(10, 6))
        plt.plot(df[x_col], df[y_col], marker='o')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid(True)
        plt.savefig(os.path.join(results_dir, filename))
        plt.close()

    # Guardar gráficos
    save_plot(df_total_utility, 'Time', 'Total Utility', 'Utilidad Total durante la Simulación', 'Tiempo',
              'Utilidad Total', 'total_utility.png')
    save_plot(df_total_traffic, 'Time', 'Total Traffic', 'Tráfico Total durante la Simulación', 'Tiempo',
              'Tráfico Total', 'total_traffic.png')

    # Función para guardar gráficos por nodo o instancia
    def save_series_plot(series_dict, title, x_label, y_label, filename):
        plt.figure(figsize=(10, 6))
        for name, series in series_dict.items():
            plt.plot(time_series, series, marker='o', label=name)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(results_dir, filename))
        plt.close()

    # Guardar gráficos por nodo e instancia
    save_series_plot(node_utility_series, 'Utilidad por Nodo', 'Tiempo', 'Utilidad', 'node_utility.png')
    save_series_plot(instance_utility_series, 'Utilidad por Instancia', 'Tiempo', 'Utilidad', 'instance_utility.png')
    save_series_plot(node_traffic_series, 'Tráfico por Nodo', 'Tiempo', 'Tráfico', 'node_traffic.png')
    save_series_plot(instance_traffic_series, 'Tráfico por Instancia', 'Tiempo', 'Tráfico', 'instance_traffic.png')

    # Guardar gráficos de cambios en recursos en nodos e instancias
    for resource_type in ['CPU', 'RAM', 'STORAGE']:
        save_series_plot(
            {name: series[resource_type] for name, series in node_resources_series.items()},
            f'Cambios en {resource_type} en Nodos',
            'Tiempo',
            f'{resource_type} Disponible',
            f'node_{resource_type.lower()}.png'
        )
        save_series_plot(
            {name: series[resource_type] for name, series in instance_resources_series.items()},
            f'Cambios en {resource_type} en Instancias',
            'Tiempo',
            f'{resource_type} Solicitado',
            f'instance_{resource_type.lower()}.png'
        )

    # Crear archivo PDF con ReportLab
    pdf_path = os.path.join(results_dir, "simulation_report.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    styleN = styles['Normal']

    # Títulos de secciones
    elements.append(Paragraph("Reporte de Simulación", styles['Title']))
    elements.append(Spacer(1, 12))  # Añadir espacio entre título y primer contenido

    # Función para añadir una tabla al PDF
    def add_table_to_pdf(elements, data, title):
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

    # Añadir gráficos al PDF
    def add_image_to_pdf(elements, image_path, title):
        elements.append(Paragraph(title, styles['Heading2']))
        elements.append(Spacer(1, 12))  # Añadir espacio entre título y gráfico
        elements.append(Image(image_path, width=500, height=300))
        elements.append(Spacer(1, 12))  # Añadir espacio entre gráficos

    # Añadir gráficos
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
        add_image_to_pdf(elements, os.path.join(results_dir, image), title)

    # Añadir tablas de datos por instancia
    for instance_name, utility_series in instance_utility_series.items():
        traffic_series = instance_traffic_series[instance_name]
        cpu_series = instance_resources_series[instance_name]['CPU']
        ram_series = instance_resources_series[instance_name]['RAM']
        storage_series = instance_resources_series[instance_name]['STORAGE']

        data = [['Tiempo', 'Utilidad', 'Tráfico', 'CPU Solicitado', 'RAM Solicitado', 'STORAGE Solicitado']]
        for i in range(len(time_series)):
            data.append([
                time_series[i],
                utility_series[i],
                traffic_series[i],
                cpu_series[i],
                ram_series[i],
                storage_series[i]
            ])
        add_table_to_pdf(elements, data, f'Datos de {instance_name}')

    # Generar PDF
    doc.build(elements)


if __name__ == '__main__':
    main()
