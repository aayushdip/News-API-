# createUser.edgeql

insert User {
  name := <str>$name,
  email := <str>$email,
  username := <str>$username,
  admin := <bool>$admin,
  subscriber := <bool>$subscriber,
  hashed_password := <str>$hashed_password
}
