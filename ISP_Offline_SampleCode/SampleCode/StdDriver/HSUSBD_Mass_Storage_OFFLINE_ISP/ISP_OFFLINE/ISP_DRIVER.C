#include "ISP_DRIVER.H"

extern ErrNo ISP_UART_WRITE(io_handle_tt handle, const void *buf, uint32 *len);
extern ErrNo ISP_UART_READ(io_handle_tt handle, void *buf, uint32 *len);
extern ErrNo UART_Config(void *priv);

CHAR_DEVIO_TABLE(
    UART_Driver,
    ISP_UART_WRITE,
    ISP_UART_READ,
)

devtab_entry_t DevTab[] =
{
    UART_NAME_STRING, &UART_Driver, UART_Config,
};

static int io_compare(const char *n1, const char *n2, const char **ptr)
{
    while (*n1 && *n2)
    {
        if (*n1++ != *n2++)
        {
            return 0;
        }
    }

    if (*n1)
    {
        // See if the devtab name is is a substring
        if (*(n2 - 1) == '/')
        {
            *ptr = n1;
            return 1;
        }
    }

    if (*n1 || *n2)
    {
        return 0;
    }

    *ptr = n1;
    return 1;
}

ErrNo  io_open(const char *dev_name, io_handle_tt *io_handle)
{
    devtab_entry_t *p_devtab_entry;
    uint32 devtab_size, i;
    const char  *name_ptr;
    ErrNo re;

    if (dev_name == 0 || io_handle == 0)
    {
        return -EINVAL;
    }

    p_devtab_entry = (devtab_entry_t *)DevTab;

    devtab_size = sizeof(DevTab) / sizeof(devtab_entry_t);

    for (i = 0; i < devtab_size; i++)
    {
        if (io_compare(dev_name, p_devtab_entry->name, &name_ptr))
        {
            if (p_devtab_entry->init)
            {
                re = p_devtab_entry->init((void *)p_devtab_entry);

                if (re != ENOERR)
                    return re;

                *io_handle = (io_handle_tt *)p_devtab_entry;
                return re;
            }
        }

        p_devtab_entry++;
    }

    return -ENOENT;
}

ErrNo io_write(io_handle_tt handle, const void *buf, uint32 *len)
{
    devtab_entry_t *t = (devtab_entry_t *)handle;

    if (handle == NULL || buf == NULL || len == NULL)
    {
        return -EINVAL;
    }

    // Validate request
    if (!t->handlers->write)
    {
        return -EDEVNOSUPP;
    }

    // Special check.  If length is zero, this just verifies that the
    // 'write' method exists for the given device.
    if (NULL != len && 0 == *len)
    {
        return ENOERR;
    }

    return t->handlers->write(handle, buf, len);
}

//
// 'read' data from a device.
//

ErrNo io_read(io_handle_tt handle, void *buf, uint32 *len)
{
    devtab_entry_t *t = (devtab_entry_t *)handle;

    if (handle == NULL || buf == NULL || len == NULL)
    {
        return -EINVAL;
    }

    // Validate request
    if (!t->handlers->read)
    {
        return -EDEVNOSUPP;
    }

    // Special check.  If length is zero, this just verifies that the
    // 'read' method exists for the given device.
    if (NULL != len && 0 == *len)
    {
        return ENOERR;
    }

    return t->handlers->read(handle, buf, len);
}
int str_compare(const char *n1, const char *n2)
{
    while (*n1 && *n2)
    {
        if (*n1++ != *n2++)
        {
            return 0;
        }
    }

    if (*n1)
    {
        // See if the devtab name is is a substring
        if (*(n2 - 1) == '/')
        {
            return 1;
        }
    }

    if (*n1 || *n2)
    {
        return 0;
    }

    return 1;
}


