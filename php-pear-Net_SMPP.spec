%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	SMPP
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - SMPP v3.4 protocol implementation
Summary(pl):	%{_pearname} - implementacja protoko³u SMPP v3.4
Name:		php-pear-%{_pearname}
Version:	0.4.3
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0ba4c28d961f753489f8463374d65ed3
URL:		http://pear.php.net/package/Net_SMPP/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_SMPP is an implementation of the SMPP (Short Message Peer-to-Peer)
v3.4 protocol. SMPP is an open protocol used in the wireless industry to
send and recieve SMS messages.

In PEAR status of this package is: %{_status}.

%description -l pl
Net_SMPP to implementacja protoko³u SMPP (Short Message Peer-to-Peer) w
wersji 3.4. SMPP to otwarty protokó³ wykorzystywany w przemy¶le
bezprzewodowym do wysy³ania i odbierania wiadomo¶ci SMS.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Command,Vendor/mBlox}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Command/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Command
install %{_pearname}-%{version}/%{_subclass}/Vendor/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Vendor
install %{_pearname}-%{version}/%{_subclass}/Vendor/mBlox/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Vendor/mBlox

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
