
select User {
  name,
  email,
  username,
  admin,
  subscriber,
  hashed_password
} filter .subscriber = true
