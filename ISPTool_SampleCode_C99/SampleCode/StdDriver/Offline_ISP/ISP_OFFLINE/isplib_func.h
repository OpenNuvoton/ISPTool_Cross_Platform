void m_dev_io_init(void);
unsigned int m_dev_io_open(void);
void m_dev_io_close(void);
unsigned int m_dev_io_read(unsigned int dwMilliseconds, unsigned char* pcBuffer);
unsigned int m_dev_io_write(unsigned int dwMilliseconds, unsigned char* pcBuffer);