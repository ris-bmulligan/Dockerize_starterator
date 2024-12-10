#!/usr/bin/env python

import os
import subprocess
import sys

from multiprocessing import Process

def run_mysqld_safe():
    if os.fork() != 0:
        return
    os.setsid()
    os.execv('/ris_mysql/safe_redirect.sh', ('' ,))

mysql_user = os.environ.get('LSFUSER', 'nobody')

for sub_dir in ['lib', 'log', 'run']:
    path = '/mysql/{}'.format(sub_dir)
    try:
        os.makedirs(path)
    except OSError:
        pass
    if sub_dir == 'lib':
        try:
            os.makedirs('{}/mysql'.format(path))
        except OSError:
            pass

data_dir =  '/mysql/lib/mysql'
error_log = '/mysql/log/error.log'
open(error_log, 'a').close()
subprocess.call(['chown', '-R', mysql_user, '/mysql'])

mysqld = {
  'mysqld_safe': {
      'socket': '/tmp/mysqld.sock',
      'nice': 0
  },
  'mysqld': {
      'user': mysql_user,
      'pid-file': '/mysql/run/mysqld.pid',
      'socket': '/tmp/mysqld.sock',
      'port': 3306,
      'basedir': '/usr',
      'datadir': data_dir,
      'tmpdir': '/tmp',
      'lc-messages-dir': '/usr/share/mysql',
      'bind-address': '127.0.0.1',
      'key_buffer_size': '16M',
      'max_allowed_packet': '16M',
      'thread_stack': '192K',
      'thread_cache_size': 8,
      'myisam-recover-options': 'BACKUP',
      'query_cache_limit': '1M',
      'query_cache_size': '16M',
      'log_error': error_log,
      'expire_logs_days': 10,
      'max_binlog_size': '100M'
  }
}

with open('/ris_mysql/mysql.conf.d/mysqld.cnf', 'w') as msc:
    for section, section_data in mysqld.items():
        msc.write('[{}]\n'.format(section))
        for k, v in section_data.items():
            msc.write('{} = {}\n'.format(k, v))
        msc.write('\n')
subprocess.call([
    '/usr/sbin/mysqld',
    '--initialize-insecure',
    '--user',
    mysql_user
])
run_mysqld_safe()
sys.exit(0)
