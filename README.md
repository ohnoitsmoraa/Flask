# Running the migrations

To run the migrations, follow the following steps:

- Initialize the flask

  `flask db init`

- Run the migration / Create migration

  `flask db migrate`

- Update migrations

  `flask db migrate -m "Message"`

- To push the update to be displayed in the database initially created

  `flask db upgrade head`
