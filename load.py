import io
import dao


def load(df, tabela):
    conn = dao.get_conn(dao.get_adrs_conn())
    cur = conn.cursor()
    output = io.StringIO()
    df.to_csv(output, header=False, index=False, sep="\t")
    output.seek(0)
    try:
        cur.copy_from(output, tabela, null="", columns=df.columns.values.tolist())
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def load_sim(df, tabela):
    conn = dao.get_conn(dao.get_adrs_conn())
    cur = conn.cursor()
    output = io.StringIO()
    df.to_csv(output, header=False, index=False, sep="\t")
    output.seek(0)
    #print(df)
    try:
        cur.copy_from(output, tabela, null="", columns=df.columns.values.tolist())
        print(output)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
