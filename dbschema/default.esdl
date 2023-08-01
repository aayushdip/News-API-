module default {
    type Company {
  required name: str;
  required founded_date: cal::local_date;
  required country: str;
  required website: str;
  required email: str {
    constraint std::regexp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$');
  }
  required contact_no: str;
}
type News {
  required title: str;
  required date_published: cal::local_date;
  required author: str;
  required section: str;
  required country: str;
}
type User{
    required name : str;
    required email: str {
  constraint exclusive;  }
    required username: str {
    constraint exclusive;
  }
  required admin : bool;
  required subscriber : bool;
  required hashed_password : str



}

}
