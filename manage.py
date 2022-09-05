def deploy():
    """Run deployment tasks."""
    from apps import create_app
    from apps.database import db
    from flask_migrate import upgrade, migrate, init, stamp

    app = create_app()
    app.app_context().push()
    db.create_all()
    
    # migrate database to latest revision
    init()
    stamp()
    migrate()
    upgrade()

def dummy():
    from werkzeug.security import generate_password_hash
    from apps import create_app
    from apps.database import db
    from apps.models import Categories, Roles, Users, Qualifications, Courses, Trainers, Enquiries

    import csv

    app = create_app()
    app.app_context().push()


    # Categories
    with open('dummy_data/categories.csv') as f:
        cr = csv.reader(f)
        header = next(cr)
        for category in cr:
            db.session.add(Categories(category[0]))
        db.session.commit()

    # Qualifications
    with open('dummy_data/qualifications.csv') as f:
        cr = csv.reader(f)
        header = next(cr)
        for q, status, level in cr:
            db.session.add(Qualifications(q, 'Enabled'==status, level))
        db.session.commit()
    
    # User roles
    for role in ['Admin', 'User']:
        db.session.add(Roles(role))
    db.session.commit()

    # Add Admin users
    db.session.add(Users('admin', '1', generate_password_hash('admin1'), 'admin@1', '6846546543', Roles.query.filter_by(role='Admin').first().id))
    db.session.add(Users('admin', '2', generate_password_hash('admin2'), 'admin@2', '6656854443', Roles.query.filter_by(role='Admin').first().id))
    db.session.add(Users('admin', '3', generate_password_hash('admin3'), 'admin@3', '6655484643', Roles.query.filter_by(role='Admin').first().id))
    db.session.add(Users('admin', '4', generate_password_hash('admin4'), 'admin@4', '6846435465', Roles.query.filter_by(role='Admin').first().id))
    db.session.add(Users('user', 'abc', generate_password_hash('user123'), 'user@foo', '6846435465', Roles.query.filter_by(role='User').first().id))
    db.session.commit()
    
    # Add normal users
    with open('dummy_data/users.csv') as f:
        password = generate_password_hash('user123')
        csvreader = csv.reader(f)
        header = next(csvreader)
        for name, email, phone in csvreader:
            db.session.add(Users(name.split()[0], ' '.join(name.split()[1:]), password, email, phone, Roles.query.filter_by(role='User').first().id))
    db.session.commit()


    # Add Trainers
    with open('dummy_data/trainers.csv') as f:
        cr = csv.reader(f)
        header = next(cr)
        for name, email, phone in cr:
            db.session.add(Trainers(name, email, phone))
        db.session.commit()


    # Add Courses
    with open('dummy_data/courses.csv') as f:
        cr = csv.reader(f)
        header = next(cr)
        for name, duration, description, comment, videolink, category, trainer, status, q in cr:
            db.session.add(Courses(
                name,
                description,
                duration,
                Categories.query.filter_by(category=category).first().id,
                Trainers.query.filter_by(name=trainer).first().id,
                videolink,
                comment,
                Qualifications.query.filter_by(qualification=q).first().id,
                'Enabled'==status
            ))
    db.session.add(Courses('Test 1', 'test test', 3, 1, 3, 'example.com', 'comment', 1, True))
    db.session.add(Courses('Test 2', 'test test', 3, 1, 3, 'example.com', 'comment', 1, True))
    db.session.add(Courses('Test 3', 'test test', 3, 1, 3, 'example.com', 'comment', 1, True))
    db.session.add(Courses('Test 4', 'test test', 3, 1, 3, 'example.com', 'comment', 1, True))
    db.session.commit()


    
    #adding some enquiries
    db.session.add(Enquiries(4, 1))
    db.session.add(Enquiries(5, 1))
    db.session.add(Enquiries(4, 2))
    db.session.commit()

if __name__ == '__main__':
    deploy()
    dummy()