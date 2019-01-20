Feature: register
  As a developer
  this is bdd first test bdd preject
  Scenario: open register website
    When I open the register website "http://www.5itest.cn/register"
    Then I except that title is "注册"
  Scenario: input username
    When I set with useremail "fan1992@163.com"
    And I set with username "fan1992"
    And I set with password "123331"
    And I set with code "jgjkdd"
    And I click registerbutton
    Then I except that text "验证码错误"
