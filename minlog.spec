%{?_javapackages_macros:%_javapackages_macros}
Name:          minlog
Version:       1.3.0
Release:       4%{?dist}
Summary:       Minimal overhead Java logging
License:       BSD
URL:           https://github.com/EsotericSoftware/minlog
Source0:       https://github.com/EsotericSoftware/minlog/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch

%description
MinLog is a Java logging library. Key features:

° Zero overhead Logging statements below a given level
  can be automatically removed by javac at compile time.
  This means applications can have detailed trace and
  debug logging without having any impact on the finished product.

° Simple and efficient The API is concise and the code
  is very efficient at run-time.

° Extremely lightweight The entire project consists of a single
  Java file with ~100 non-comment lines of code.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find -name "*.class" -delete
find -name "*.jar" -delete

%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:executions"

sed -i 's/\r//' license.txt

%mvn_file :%{name} %{name}
%mvn_alias :%{name} "com.googlecode:%{name}" "com.esotericsoftware.%{name}:%{name}"
%mvn_package ":%{name}::tests:"

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 gil cattaneo <puntogil@libero.it> 1.3.0-1
- update to 1.3.0

* Wed May 20 2015 gil cattaneo <puntogil@libero.it> 1.2-8
- fix Url and Source0 tag

* Tue Feb 10 2015 gil cattaneo <puntogil@libero.it> 1.2-7
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.2-5
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 05 2013 gil cattaneo <puntogil@libero.it> 1.2-3
- switch to XMvn
- minor changes to adapt to current guideline

* Tue Apr 30 2013 gil cattaneo <puntogil@libero.it> 1.2-2
- installed proper license file

* Fri Mar 08 2013 gil cattaneo <puntogil@libero.it> 1.2-1
- initial import for fedora

* Thu Aug 4 2011 gil <puntogil@libero.it> 1.2-mga1
- initial rpm
