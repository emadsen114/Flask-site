from website import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # runs our flask application 

# only if we run this file does this line get executed

