%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	SMPP
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - SMPP v3.4 protocol implementation
Summary(pl):	%{_pearname} - implementacja protoko³u SMPP v3.4
Name:		php-pear-%{_pearname}
Version:	0.4.3
Release:	1.1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0ba4c28d961f753489f8463374d65ed3
URL:		http://pear.php.net/package/Net_SMPP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_SMPP is an implementation of the SMPP (Short Message Peer-to-Peer)
v3.4 protocol. SMPP is an open protocol used in the wireless industry
to send and recieve SMS messages.

In PEAR status of this package is: %{_status}.

%description -l pl
Net_SMPP to implementacja protoko³u SMPP (Short Message Peer-to-Peer)
w wersji 3.4. SMPP to otwarty protokó³ wykorzystywany w przemy¶le
bezprzewodowym do wysy³ania i odbierania wiadomo¶ci SMS.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
