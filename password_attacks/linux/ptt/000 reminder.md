# OVERVIEW
| Situation                            | Keytab present? | ccache present?                           |
| ------------------------------------ | --------------- | ----------------------------------------- |
| User logs in with password (`kinit`) | No              | Yes                                       |
| Service account using keytab         | Yes             | Usually yes after authentication          |
| Fresh system before authentication   | Maybe           | No                                        |
| Expired tickets                      | Maybe           | ccache file may exist but tickets invalid |



# CCACHE
- linux commonly store kerberos tickets as `ccache` files in the `/tmp`
- to abuse a ccache file, all we need is `read` privileges on the file.
- location of the ticket = `KRB5CCNAME` (env var)
- `elevated privileges` or `root privileges` needed



# KEYTAB
- every pc with a kerberos client can create `keytab files`
- contains pairs of kerberos principals and encrypted keys (derived from Kerberos password)
- if pw changed > recreate all keytab files
- commonly allow scripts to authenticate automatically using kerberos
- keytab files are not restricted to the systems on which they were created.
- to use a keytab file, we need `rw`
- `/etc/krb5.keytab`








