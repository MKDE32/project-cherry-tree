# overview
- chisel uses socks5 tunneling

# capabilitys
- platform independent
- no admin rights needed if:
  - port > 1024
  - user rights
  - outgoing traffic allowed
- adminright needed if
  - virtual netadapter

# static build
- if you build chisel by your own you will need to use go
- it is necessary to build the same version on attacker and target.
- to do so we need to use a `static clib build`
- to do so we use the `CGO_ENABLED=0` variable
- to check it we can use `file chisel` or `ldd chisel`

# reverse
```
      ATTACKER        |            | WEBSERVER  |           |    WIN1    |
                      |            |            |           |            |
                    1234 < --    random         |           |            |
xfreerdp -> 1080 ->   |  -- >      |         random  -- >  3389          |
                      |            |            |           |            |
      SERVER          |            |  CLIENT    |           |   SERVER   |
```
# reverse double
```
      ATTACKER        |            | WEBSERVER  |           |    WIN1    |          |  DC01
                      |            |            |           |            |          |
                    1234 < --    random         |           |            |          |
xfreerdp -> 1080 ->   |  -- >      |            |           |         random -- > 3389
                      |            |            |           |            |          |
      SERVER          |            |  CLIENT    |           |   SERVER   |          |
```














# forward
- attacker -> victim
  - client = attacker
  -  server = victim
