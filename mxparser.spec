Name:           mxparser
Version:        1.2.1
Release:        3
License:        Lab Software License
Summary:        MXParser is a fork of xpp3_min 1.1.7 containing only the parser with merged changes of the Plexus fork.
URL:            http://x-stream.github.io/mxparser
Source0:        https://github.com/x-stream/mxparser/archive/refs/tags/v-1.2.1.tar.gz
Source1:        settings.xml
Source2:        repository.tar.gz
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
mkdir -p /home/abuild/.m2
tar -xf %{SOURCE2} -C /home/abuild/.m2/

%build
mvn install --settings ./settings.xml -Dmaven.test.skip=true
%mvn_build -f -s -b -- -Dversion.java.source=8

%install
%mvn_install

%files -f .mfiles-mxparser
%doc changes.xml LICENSE.txt README.md

%files help -f .mfiles-javadoc

%changelog
* Mon Mar 28 2022 xiaoqianlv <xiaoqian@nj.iscas.ac.cn> - 1.2.1-3
- upload repository due to network connection timeout

* Wed Jul 21 2021 lingsheng <lingsheng@huawei.com> - 1.2.1-2
- Change maven repository to huawei cloud

* Tue Apr 13 2021 wutao <wutao61@huawei.com> - 1.2.1-1
- package init
