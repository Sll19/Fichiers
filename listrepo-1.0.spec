Name:           listrepo
Version:        1.0
Release:        1%{?dist}
Summary:        List repos script
Group:		Miscellaneous
License:        License text
# URL:            
Source0:	listrepo-1.0.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)      

# BuildRequires:  
# Requires:       

%description
List Centreon repos

%prep

%setup -q

%build
# %configure
# make %{?_smp_mflags}


%install

rm -rf $RPM_BUILD_ROOT

# %make_install

install -d -m 0755 $RPM_BUILD_ROOT/opt/listrepo
install -m 0755 listrepo.sh $RPM_BUILD_ROOT/opt/listrepo/listrepo.sh

%clean

rm -rf $RPM_BUILD_ROOT

%files

# %doc

/opt/listrepo/listrepo.sh

%changelog
