%define debug_package %{nil}

Name:       aspell-en
Summary:    English dictionaries for Aspell
Version:    2018.04.16
Release:    1
Group:      Applications/Text
BuildArch:  noarch
License:    MIT and BSD
URL:        http://aspell.net/
Source0:    %{name}-%{version}.tar.gz
Requires:   aspell >= 0.60
BuildRequires:  aspell >= 0.60

%description
Provides the word list/dictionaries for the following: English, Canadian
English, British English

%prep
%setup -q -n %{name}-%{version}/aspell-en

%build
./configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%doc Copyright
%{_libdir}/aspell-0.60/*


