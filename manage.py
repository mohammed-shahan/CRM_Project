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

def dummy():
    from apps import create_app
    from apps.database import db
    from apps.models import Categories

    app = create_app()
    app.app_context().push()

    for category in set('Lorem ipsum dolor sit amet consectetur adipiscing elit Donec vel sem nulla Curabitur feugiat hendrerit quam eleifend venenatis Morbi nulla dolor dictum ut rutrum at fermentum a felis Fusce tincidunt aliquam elementum Sed sollicitudin leo lorem id luctus quam rutrum et Maecenas vitae vehicula nisi Proin sit amet lectus eu sapien dictum dictum Aenean vulputate risus'.split()):
        db.session.add(Categories(category))
    db.session.commit()
    

if __name__ == '__main__':
    deploy()