#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-HikariCP-java7
Version  : 2.4.12
Release  : 2
URL      : https://github.com/brettwooldridge/HikariCP/archive/HikariCP-2.4.12.tar.gz
Source0  : https://github.com/brettwooldridge/HikariCP/archive/HikariCP-2.4.12.tar.gz
Source1  : https://repo1.maven.org/maven2/com/zaxxer/HikariCP-java7/2.4.12/HikariCP-java7-2.4.12.jar
Source2  : https://repo1.maven.org/maven2/com/zaxxer/HikariCP-java7/2.4.12/HikariCP-java7-2.4.12.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-HikariCP-java7-data = %{version}-%{release}

%description
<h1>![](https://github.com/brettwooldridge/HikariCP/wiki/Hikari.png) HikariCP<sup><sup>&nbsp;It's Faster.</sup></sup><sub><sub><sup>Hi·ka·ri [hi·ka·'lē] &#40;*Origin: Japanese*): light; ray.</sup></sub></sub></h1><br>
[![][Build Status img]][Build Status]
[![][Issue Stats img]][Issue Stats]
[![][Coverage Status img]][Coverage Status]
[![][Dependency Status img]][Dependency Status]
[![][license img]][license]
[![][Maven Central img]][Maven Central]

%package data
Summary: data components for the mvn-HikariCP-java7 package.
Group: Data

%description data
data components for the mvn-HikariCP-java7 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/zaxxer/HikariCP-java7/2.4.12
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/zaxxer/HikariCP-java7/2.4.12/HikariCP-java7-2.4.12.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/zaxxer/HikariCP-java7/2.4.12
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/zaxxer/HikariCP-java7/2.4.12/HikariCP-java7-2.4.12.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/zaxxer/HikariCP-java7/2.4.12/HikariCP-java7-2.4.12.jar
/usr/share/java/.m2/repository/com/zaxxer/HikariCP-java7/2.4.12/HikariCP-java7-2.4.12.pom
