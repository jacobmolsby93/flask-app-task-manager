from taskmanager import db

class Category(db.Model):
    # Schema for the Category model
    # dot notation is to specify the columns.
    id = db.Column(db.Integer, primary_key=True)
    # db.string(25) = max char 25. unique = each new added category in the database
    # should be unique. last, the nullable=False == field required.
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    # self is similiar to this in javascript.
    def __repr_(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name

class Task(db.Model):
    # Schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    # if you wanted to inlclude time, db.DateTime | db.Time.
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr_(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
    )
