Name:           mxparser
Version:        1.2.1
Release:        1
License:        Lab Software License
Summary:        MXParser is a fork of xpp3_min 1.1.7 containing only the parser with merged changes of the Plexus fork.
URL:            http://x-stream.github.io/mxparser
Source0:        https://github.com/x-stream/mxparser/archive/refs/tags/v-1.2.1.tar.gz
Source1:        settings.xml
BuildRequires:  javapackages-local java-javadoc xmlpull maven-local maven
BuildArch:      noarch

%description
MXParser is a fork of xpp3_min 1.1.7 containing only the parser with merged changes of the Plexus fork.

%package       help
Summary:       Help documents for mxparser
%description   help
Help documents for mxparser.

%prep
%autosetup -n %{name}-v-%{version}
%pom_remove_plugin :maven-bundle-plugin
%pom_remove_plugin :maven-jar-plugin
%pom_remove_plugin :maven-source-plugin
cp -a %{_sourcedir}/settings.xml .

%build
mvn install --settings ./settings.xml -Dmaven.test.skip=true
%mvn_build -f -s -b -- -Dversion.java.source=8

%install
%mvn_install

%files -f .mfiles-mxparser
%doc changes.xml LICENSE.txt README.md

%files help -f .mfiles-javadoc

%changelog
* Tue Apr 13 2021 wutao <wutao61@huawei.com> - 1.2.1-1
- package init
