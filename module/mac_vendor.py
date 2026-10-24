from mac_vendor_lookup import MacLookup, VendorNotFoundError

mac_lookup = MacLookup()


def mac_vendor(set_mac: str) -> str:
    try:
        return mac_lookup.lookup(set_mac)
    except VendorNotFoundError:
        return "Unknown vendor"