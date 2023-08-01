CREATE MIGRATION m1j4ya3ob6iz2d3o26taphgrzn3sbh6b6hkgxxfvofyy7vooyol2la
    ONTO m1fklp5rz4cz34nopkwenuzh6jxxc5x2rmkcdsxtr23wmkmbpivs5q
{
  ALTER TYPE default::User {
      ALTER PROPERTY email {
          CREATE CONSTRAINT std::exclusive;
      };
  };
  ALTER TYPE default::User {
      ALTER PROPERTY email {
          DROP CONSTRAINT std::regexp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$');
      };
  };
};
