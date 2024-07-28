import pytest
import allure
from axe_selenium_python import Axe
import json
import os
from config.links import Links

@pytest.mark.usefixtures("driver")
class TestAccessibility:
    @allure.description("Test the accessibility of the webpage using Axe")
    @allure.step("Navigating to the webpage")
    def test_accessibility(self):
        self.driver.get(Links.Host)

        axe = Axe(self.driver)
        axe.inject()
        results = axe.run()

        with open('received_data/axe-results.json', 'w') as f:
            json.dump(results, f, indent=4)

        filtered_results = [violation for violation in results['violations'] if
                            violation['id'] not in ['html-has-lang', 'landmark-one-main', 'page-has-heading-one']]

        if filtered_results:
            print("Accessibility violations found:")
            for violation in filtered_results:
                print(f"\nViolation ID: {violation['id']}")
                print(f"Description: {violation['description']}")
                print(f"Impact: {violation['impact']}")
                print(f"Help URL: {violation['helpUrl']}")
                print(f"Nodes: {len(violation['nodes'])}")
                for node in violation['nodes']:
                    print(f"  Target: {node['target']}")
                    print(f"  Failure Summary: {node.get('failureSummary', 'No failure summary available')}")

        assert not filtered_results, f"Accessibility violations found: {filtered_results}"