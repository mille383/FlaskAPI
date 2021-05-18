from app import app, db

# app = create_app()

@app.shell_context_processor
def make_shell_context():
    # ALWAYS HAVE TO RETURN A PYTHON DICTIONARY FROM CONTEXT
    return {
        'db': db,
    }