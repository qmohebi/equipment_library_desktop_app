from ldap3 import Server, Connection, ALL, AUTO_BIND_TLS_BEFORE_BIND


class LDAPAuthentication:
    def __init__(self, ldap_server: str, serach_base: str) -> None:
        self.ldap_server = ldap_server
        self.search_base = serach_base
        self.server = Server(host=self.ldap_server, get_info=ALL)

    def authenticate(self, username: str, password: str) -> bool:
        """uses the username and password provided to bind to the ldap server
        if username and password correct, return true, else return false"""
        try:
            # Establish connection
            with Connection(
                self.server,
                user=f"{username}",
                password=password,
                authentication="SIMPLE",
                auto_bind=AUTO_BIND_TLS_BEFORE_BIND,
                read_only=True,
                raise_exceptions=True,
            ) as conn:
                print(conn)
                if conn.bind():
                    return True

                else:
                    return False

        except Exception as e:
            return f"Authentication failed: {e}"


if __name__ == "__main__":
    auth = LDAPAuthentication(
        ldap_server="net.stgeorges.nhs.uk",
        serach_base="DC=net,DC=stgeorges,DC=nhs,DC=uk",
    )
    auth.authenticate("", "")
