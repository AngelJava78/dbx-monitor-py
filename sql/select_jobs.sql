SELECT
    job_id,
    job_name,
    run_id,
    started_cdmx,
    ended_cdmx,
    duration,
    result_state,
    proceso,
    subproceso,
    etapa,
    subetapa
FROM public.runs;
