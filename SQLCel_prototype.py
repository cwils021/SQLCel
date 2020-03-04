from flask import Flask, request, jsonify
import flask_excel as excel
import pandas as pd
import pandasql as psql

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        array = request.get_array(field_name='file')
        cols = array.pop(0)
        
        df = pd.DataFrame(array, columns=cols)
        df.drop(df.columns[0], axis=1, inplace=True)
        
        pysqldf = lambda q: sqldf(q, locals())
        
        q = """SELECT SG, Boiler_type, count(Boiler_type) as count
            FROM df
            GROUP BY SG, Boiler_type """
        
        query = psql.sqldf(q, locals())
        print(query)
        results = pd.DataFrame.to_html(query)
        
        return results
        
         
        
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''





# insert database related code here
if __name__ == "__main__":
    excel.init_excel(app)
    app.run(debug=True)