import datetime
import operator
import os
from pprint import pprint
from unittest import (
    TestCase,
    TestLoader,
    TextTestResult,
    TextTestRunner)

import testlink
from lxml import etree
# import subprocess
from test_module import *
from test_module2 import *

# args = ["python", "test_module.py"]
# subprocess.call(args)
# tls.reportTCResult(a_TestCaseID, a_TestPlanID, 'a build name', 'f', 'some notes', user='a user login name', platformid=a_platformID)

# https://www.reddit.com/r/learnpython/comments/28eoz9/python_unittest_do_something_different_if_test/


# suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
# out = unittest.TextTestRunner(verbosity=2).run(suite)
# print (out)
OK = 'ok'
FAIL = 'fail'
ERROR = 'error'
SKIP = 'skip'


class JsonTestResult(TextTestResult):

    def __init__(self, stream, descriptions, verbosity):
        super_class = super(JsonTestResult, self)
        super_class.__init__(stream, descriptions, verbosity)

        # TextTestResult has no successes attr
        self.successes = []

    def addSuccess(self, test):
        # addSuccess do nothing, so we need to overwrite it.
        super(JsonTestResult, self).addSuccess(test)
        self.successes.append(test)

    def json_append(self, test, result, out):
        suite = test.__class__.__name__
        if suite not in out:
            out[suite] = {OK: {}}
        if result is OK:
            out[suite][OK][test._testMethodName] = 'p'
        elif result is FAIL:
            out[suite][OK][test._testMethodName] = 'f'
        elif result is ERROR:
            out[suite][OK][test._testMethodName] = 'e'
        elif result is SKIP:
            out[suite][OK][test._testMethodName] = 'n'
        else:
            raise KeyError("No such result: {}".format(result))
        return out

    def jsonify(self):
        json_out = dict()
        for t in self.successes:
            json_out = self.json_append(t, OK, json_out)

        for t, _ in self.failures:
            json_out = self.json_append(t, FAIL, json_out)

        for t, _ in self.errors:
            json_out = self.json_append(t, ERROR, json_out)

        for t, _ in self.skipped:
            json_out = self.json_append(t, SKIP, json_out)
        return json_out


if __name__ == '__main__':
    # redirector default output of unittest to /dev/null
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
with open(os.devnull, 'w') as null_stream:
    # new a runner and overwrite resultclass of runner
    runner = TextTestRunner(stream=null_stream)
    runner.resultclass = JsonTestResult

    # create a testsuite
    suite = TestLoader().loadTestsFromTestCase(TestSimple)

    # run the testsuite
    result = runner.run(suite)

    # print json output
    # pprint(result.jsonify())

    TESTLINK_API_PYTHON_SERVER_URL = "http://192.168.43.122/lib/api/xmlrpc/v1/xmlrpc.php"
    TESTLINK_API_PYTHON_DEVKEY = "425a0eba97d42c8005a07c7613e359c1"

    # tls = testlink.TestLinkHelper( TESTLINK_API_PYTHON_SERVER_URL, TESTLINK_API_PYTHON_DEVKEY).connect(testlink.TestlinkAPIClient)

    tlh = testlink.TestLinkHelper(TESTLINK_API_PYTHON_SERVER_URL, TESTLINK_API_PYTHON_DEVKEY)
    tls = testlink.TestlinkAPIClient(tlh._server_url, tlh._devkey, verbose=False)

    print("\n\nProjects count: " + str(tls.countProjects()) + "\n\n")

    tc_info = tls.getTestCase(None, testcaseexternalid='1-1')
    # print("\n\n" + str(tc_info) + "\n\n")

    tc_info = tls.getProjectTestPlans('1')
    # print("\n\n" + str(tc_info) + "\n\n")
    # tls.reportTCResult(4, 2, 'SampleBuild', 'f', 'some notes', user='user', platformid='1')
    date = str(datetime.datetime.now())
    date.replace("-", "/")
    date = date[:-7]
    steps_result = result.jsonify()['TestSimple']['ok']
    steps_result2 = sorted(steps_result.keys())
    test_passed = 'p'

    if 'n' in steps_result.values(): test_passed = 'p'
    if 'e' in steps_result.values(): test_passed = 'p'
    if 'f' in steps_result.values(): test_passed = 'p'

    print(steps_result)

    tls.reportTCResult(None, 2, None, test_passed, 'DPP_lab10_test1', guess=True,
                       testcaseexternalid='1-1',
                       platformname='NewPlatform',
                       execduration=TestSimple.elapsed, timestamp=str(date),
                       steps=[{'step_number': 1, 'result': steps_result.get(steps_result2[0]),
                               'notes': 'result note for passed step 1'},
                              {'step_number': 2, 'result': steps_result.get(steps_result2[1]),
                               'notes': 'result note for passed step 2'},
                              {'step_number': 3, 'result': steps_result.get(steps_result2[2]),
                               'notes': 'result note for passed step 3'},
                              {'step_number': 4, 'result': steps_result.get(steps_result2[3]),
                               'notes': 'result note for passed step 4'},
                              {'step_number': 5, 'result': steps_result.get(steps_result2[4]),
                               'notes': 'result note for passed step 5'},
                              {'step_number': 6, 'result': steps_result.get(steps_result2[5]),
                               'notes': 'result note for passed step 6'}])

    # create a testsuite
    suite = TestLoader().loadTestsFromTestCase(TestSimple2)

    # run the testsuite
    result = runner.run(suite)

    tc_info = tls.getTestCase(None, testcaseexternalid='1-2')
    # print("\n\n" + str(tc_info) + "\n\n")

    tc_info = tls.getProjectTestPlans('1')
    # print("\n\n" + str(tc_info) + "\n\n")
    # tls.reportTCResult(4, 2, 'SampleBuild', 'f', 'some notes', user='user', platformid='1')
    date = str(datetime.datetime.now())
    date.replace("-", "/")
    date = date[:-7]
    steps_result = result.jsonify()['TestSimple2']['ok']
    steps_result2 = sorted(steps_result.keys())
    test_passed = 'p'

    if 'n' in steps_result.values(): test_passed = 'p'
    if 'e' in steps_result.values(): test_passed = 'p'
    if 'f' in steps_result.values(): test_passed = 'p'

    tls.reportTCResult(None, 2, None, test_passed, 'DPP_lab10_test2', guess=True,
                       testcaseexternalid='1-2',
                       platformname='NewPlatform',
                       execduration=3.90, timestamp=str(date),
                       steps=[{'step_number': 1, 'result': steps_result.get(steps_result2[0]),
                               'notes': 'result note for passed step 1'},
                              {'step_number': 2, 'result': steps_result.get(steps_result2[1]),
                               'notes': 'result note for passed step 2'},
                              {'step_number': 3, 'result': steps_result.get(steps_result2[2]),
                               'notes': 'result note for passed step 3'},
                              {'step_number': 4, 'result': steps_result.get(steps_result2[3]),
                               'notes': 'result note for passed step 4'},
                              {'step_number': 5, 'result': steps_result.get(steps_result2[4]),
                               'notes': 'result note for passed step 5'},
                              {'step_number': 6, 'result': steps_result.get(steps_result2[5]),
                               'notes': 'result note for passed step 6'},
                              {'step_number': 7, 'result': steps_result.get(steps_result2[6]),
                               'notes': 'result note for passed step 7'}])
