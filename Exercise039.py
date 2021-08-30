def generate_sql(table_name, col_names,constraints):
    columns = [" ".join((col, constraints)).strip() for col, constraints in zip(col_names,constraints)]
    return f'CREATE TABLE {table_name} (' + ', '.join(columns) + ')'