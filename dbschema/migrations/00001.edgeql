CREATE MIGRATION m1qz64pcamrvnxe7oz5nh53lshadcgk7vu7xe6xxzhf56q7i6adbta
    ONTO initial
{
  CREATE TYPE default::Company {
      CREATE REQUIRED PROPERTY contact_no: std::str;
      CREATE REQUIRED PROPERTY country: std::str;
      CREATE REQUIRED PROPERTY email: std::str {
          CREATE CONSTRAINT std::regexp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$');
      };
      CREATE REQUIRED PROPERTY founded_date: cal::local_date;
      CREATE REQUIRED PROPERTY name: std::str;
      CREATE REQUIRED PROPERTY website: std::str;
  };
  CREATE TYPE default::News {
      CREATE REQUIRED PROPERTY author: std::str;
      CREATE REQUIRED PROPERTY country: std::str;
      CREATE REQUIRED PROPERTY date_published: cal::local_date;
      CREATE REQUIRED PROPERTY section: std::str;
      CREATE REQUIRED PROPERTY title: std::str;
  };
  CREATE TYPE default::User {
      CREATE REQUIRED PROPERTY admin: std::bool;
      CREATE REQUIRED PROPERTY email: std::str {
          CREATE CONSTRAINT std::regexp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$');
      };
      CREATE PROPERTY hashed_password: std::str;
      CREATE REQUIRED PROPERTY name: std::str;
      CREATE PROPERTY subscriber: std::bool;
      CREATE REQUIRED PROPERTY username: std::str {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
