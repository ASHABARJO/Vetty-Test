from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', defaults={'filename': 'file1.txt'}, methods=['GET'])
def render_file(filename):
    try:
        start_line = request.args.get('start', type=int)
        end_line = request.args.get('end', type=int)
        
        with open(filename, 'r', encoding='utf-8') as file:
            file_lines = file.readlines()

        if start_line is not None and end_line is not None:
            file_content = ''.join(file_lines[start_line-1:end_line])
        else:
            file_content = ''.join(file_lines)

        return render_template('render.html', filename=filename, file_content=file_content)
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
