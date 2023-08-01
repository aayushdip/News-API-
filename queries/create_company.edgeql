# createCompany.edgeql

insert Company {
  name := <str>$name,
  founded_date := <cal::local_date>$founded_date,
  country := <str>$country,
  website := <str>$website,
  email := <str>$email,
  contact_no := <str>$contact_no
}
