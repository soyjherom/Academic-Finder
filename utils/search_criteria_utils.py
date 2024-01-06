def get_search_criteria(args):
  query="query="+ args.query if args.query else ""
  date_from_year = args.from_year
  date_to_year = args.to_year
  if query:
    query = "search?" + query
  if date_from_year:
    query += "&dateFromYear=" + date_from_year
  if date_to_year:
    query += "&dateToYear=" + date_to_year
  return query

def get_form_data_criteria(args):
  query = args.query
  date_from_year = args.from_year
  date_to_year = args.to_year
  return {
    "query": query,
    "dateFromYear": date_from_year,
    "dateToYear": date_to_year
  }