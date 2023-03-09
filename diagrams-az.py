from diagrams import Diagram
from diagrams.azure.integration import APIManagement
from diagrams.azure.compute import KubernetesServices
from diagrams.azure.identity import ActiveDirectory
from diagrams.onprem.client import Users
from diagrams.onprem.container import Docker
from diagrams.programming.language import Python
from diagrams.generic.os import Windows
from diagrams.azure.database import SQLDatabases, CosmosDb
from diagrams.azure.web import AppServiceEnvironments

with Diagram("Azure Microservices Architecture", show=False):
    k8s = KubernetesServices("Kubernetes")
    api_management = APIManagement("API Management")
    user_management = Docker("User Management Service")
    product_catalog = Docker("Product Catalog Service")
    order_processing = Docker("Order Processing Service")
    web_app = AppServiceEnvironments("Web App")
    auth = ActiveDirectory("Authentication and Authorization")
    sql_db = SQLDatabases("SQL Azure Database")
    cosmos_db = CosmosDb("CosmosDB")
    user = Users("User")
    python = Python("Python")
    docker = Docker("Docker")
    windows = Windows("Windows")

    user >> api_management >> k8s >> [product_catalog, order_processing, user_management] >> sql_db
    product_catalog >> cosmos_db
    order_processing >> cosmos_db
    web_app >> api_management
    auth >> api_management
    python >> docker >> windows
    sql_db >> docker >> windows

    # Export the diagram as SVG image
    diag = Diagram("Azure Microservices Architecture", show=False)
#    diag.add(k8s, api_management, user_management, product_catalog, order_processing, web_app, auth, sql_db, cosmos_db, user, python, windows)
#    diag.save("architecture.svg")
