CREATE MIGRATION m1fklp5rz4cz34nopkwenuzh6jxxc5x2rmkcdsxtr23wmkmbpivs5q
    ONTO m1qz64pcamrvnxe7oz5nh53lshadcgk7vu7xe6xxzhf56q7i6adbta
{
  ALTER TYPE default::User {
      ALTER PROPERTY hashed_password {
          SET REQUIRED USING (<std::str>{});
      };
      ALTER PROPERTY subscriber {
          SET REQUIRED USING (<std::bool>{});
      };
  };
};
