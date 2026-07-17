select distinct result_state
  from public.runs
 where result_state is not null
 order by result_state;