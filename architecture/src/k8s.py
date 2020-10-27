# archi_general.py
from diagrams import Cluster, Diagram
from diagrams.k8s.rbac import User
from diagrams.k8s.network import Ingress
from diagrams.k8s.network import Service
from diagrams.k8s.compute import Pod

with Diagram("Corpo k8s Service", show=True,direction="TB"):

    user = User()

    #external from Decathlon nextwork
    with Cluster("k8s"):
        ing = Ingress("")
        srv = Service("")
        pod = Pod("Corpo app")

    user >> ing >> srv >> pod    