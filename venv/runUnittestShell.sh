

find . -name "run_test_module.py" -print | while read f; do
        echo "$f"
        ###
        python -m coverage run "$f"
        python -m coverage xml -o coverage.xml
        ###
done

cp -r ./coverage.xml ~/Downloads/jenkins_2.127_all/data/var/lib/jenkins/workspace/DPP_lab12/coverage.xml
cp -r ./python_unittests_xml ~/Downloads/jenkins_2.127_all/data/var/lib/jenkins/workspace/DPP_lab12/python_unittests_xml