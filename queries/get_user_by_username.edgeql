# getUserByUsername.edgeql

select User {
  name,
  email,
  username,
  admin,
  subscriber,
  hashed_password
} filter .username = <str>$0
