# Adjust the code to use proper edge definitions
from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Kafka Architecture Diagram')

# Add nodes for each component
dot.node('App', 'Application')
dot.node('Prod', 'Producers')
dot.node('Kafka', 'Kafka Cluster')
dot.node('Brokers', 'Brokers')
dot.node('Topics', 'Topics')
dot.node('Partitions', 'Partitions')
dot.node('Zoo', 'ZooKeeper')
dot.node('Cons', 'Consumers')
dot.node('Connect', 'Kafka Connect')
dot.node('Streams', 'Kafka Streams')
dot.node('ExtSys', 'External Systems')

# Add edges to show the data flow
dot.edge('App', 'Prod')
dot.edge('Prod', 'Kafka')
dot.edge('Kafka', 'Brokers')
dot.edge('Brokers', 'Topics')
dot.edge('Topics', 'Partitions')
dot.edge('Zoo', 'Kafka')
dot.edge('Kafka', 'Cons')
dot.edge('Kafka', 'Connect')
dot.edge('Kafka', 'Streams')
dot.edge('Connect', 'ExtSys')
dot.edge('Streams', 'Cons')

# Render the diagram
diagram_path = '/tmp/kafka_architecture_diagram'
dot.render(diagram_path, format='png')

# Display the path to the generated diagram
diagram_path + '.png'
