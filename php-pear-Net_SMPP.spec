%define		_status		beta
%define		_pearname	Net_SMPP
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - SMPP v3.4 protocol implementation
Summary(pl.UTF-8):	%{_pearname} - implementacja protokołu SMPP v3.4
Name:		php-pear-%{_pearname}
Version:	0.4.5
Release:	3
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2ceb72287a4f6de3f8fab91f80a3ca34
URL:		http://pear.php.net/package/Net_SMPP/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.1.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.3
Suggests:	php-pear-Net_Socket
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Net/Socket.*)

%description
Net_SMPP is an implementation of the SMPP (Short Message Peer-to-Peer)
v3.4 protocol. SMPP is an open protocol used in the wireless industry
to send and recieve SMS messages.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Net_SMPP to implementacja protokołu SMPP (Short Message Peer-to-Peer)
w wersji 3.4. SMPP to otwarty protokół wykorzystywany w przemyśle
bezprzewodowym do wysyłania i odbierania wiadomości SMS.

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
%{php_pear_dir}/Net/*.php
%{php_pear_dir}/Net/SMPP
