from airflow.sdk import dag, task

@dag(
    dag_id="gaming_telemetry_pipeline",
    schedule=None,
    catchup=False,
    tags=["gaming", "data-engineering"],
)
def gaming_telemetry_pipeline():
    pass

gaming_telemetry_pipeline()