def deploy():
    """Run deployment tasks."""
    from apps import create_app
    from apps.database import db
    from flask_migrate import upgrade, migrate, init, stamp
    from apps.models import Users

    app = create_app()
    app.app_context().push()
    db.create_all()
    
    # migrate database to latest revision
    init()
    stamp()
    migrate()
    upgrade()



if __name__ == '__main__':
    deploy()