- build.sbt
    - Scala Build Tool
    - Scale脚本，build一个java project
        - 如何使用 ？
            - 

    - lazy val root = (project in file(".")).enablePlugins(PlayJava, PlayEbean, RpmPlugin, SystemdPlugin)
        - lazy val root
            - sbt evaluates things recursively, and using laziness helps to avoid out of order evaluation. root in this case is the name we gave to the subproject.
        - (project in file("."))
            - In sbt world, project is an ambiguous word, so projects defined in build.sbt are often called subprojects. In this build, the subproject root is in the root directory. If we decide to add another subproject, we could use something like lazy val app = (project in file("app")).

    - Command 'sbt' not found
        - https://www.scala-sbt.org/release/docs/Installing-sbt-on-Linux.html#Ubuntu+and+other+Debian-based+distributions
            - 亲测有效

    - /usr/bin/sbt: line 468: java: command not found
        - 

- rpm
    - Although it was created for use in Red Hat Linux, RPM is now used in many Linux distributions such as PCLinuxOS, Fedora, AlmaLinux, CentOS, openSUSE, OpenMandriva and Oracle Linux. It has also been ported to some other operating systems, such as Novell NetWare (as of version 6.5 SP3), IBM's AIX (as of version 4),[7] IBM i,[8] and ArcaOS.[9]
    - ubuntu也有
