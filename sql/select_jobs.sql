SELECT
    r.job_id,
    r.job_name,
    r.run_id,
    r.started_cdmx,
    r.ended_cdmx,
    r.duration,
    r.result_state,
    r.proceso,
    r.subproceso,
    r.etapa,
    r.subetapa,
    ss.substage_name
FROM public.runs r 
LEFT JOIN public.substages ss
    ON NULLIF(TRIM(r.subetapa::TEXT), '')::INT4 = ss.substage_id;
