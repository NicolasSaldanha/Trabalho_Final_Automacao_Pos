from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
  def __init__(self, driver):
     self._driver = driver 

  def wait_load(self):
    elements = self._driver.find_elements(By.CSS_SELECTOR, ".smooth")  
    while len(elements) > 0:
        elements = self._driver.find_elements(By.CSS_SELECTOR, ".smooth")
        sleep(1)

  def add_aluno(self, aluno):
    self._driver.find_element(By.ID, "student-nome").click()
    student_name_input = self._driver.find_element(By.ID, "student-nome")
    student_name_input.clear()
    self._driver.find_element(By.ID, "student-nome").send_keys(aluno)
    self._driver.find_element(By.ID, "student-btn").click()
      
  def add_curso(self,curso):
    self._driver.find_element(By.ID, "course-nome").click()
    element = self._driver.find_element(By.ID, "course-nome")
    actions = ActionChains(self._driver)
    actions.double_click(element).perform()
    element.clear()
    self._driver.find_element(By.ID, "course-nome").send_keys(curso)
    self._driver.find_element(By.ID, "course-btn").click()

  def add_disciplina(self, disciplina, id):
      self._driver.find_element(By.ID, "discipline-nome").click()
      disciplina_input = self._driver.find_element(By.ID, "discipline-nome")
      disciplina_input.clear()
      self._driver.find_element(By.ID, "discipline-nome").send_keys(disciplina)
      self._driver.find_element(By.ID, "course-discipline-id").click()
      disciplina_ID_input = self._driver.find_element(By.ID, "course-discipline-id")
      disciplina_ID_input.clear()
      self._driver.find_element(By.ID, "course-discipline-id").send_keys(id)
      self._driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()

  def sub_to_course(self, std_id, course_id):
      self._driver.find_element(By.ID, "student-id").click()
      std_ID_input = self._driver.find_element(By.ID, "student-id")
      std_ID_input.clear()
      self._driver.find_element(By.ID, "student-id").send_keys(std_id)
      self._driver.find_element(By.ID, "course-id").click()
      course_ID_input = self._driver.find_element(By.ID, "course-id")
      course_ID_input.clear()
      self._driver.find_element(By.ID, "course-id").send_keys(course_id)
      self._driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn").click()

  def sub_to_disciplina(self, std_id, disc_id):
      self._driver.find_element(By.ID, "subscribe-student-id").click()
      std_ID_input = self._driver.find_element(By.ID, "subscribe-student-id")
      std_ID_input.clear()
      self._driver.find_element(By.ID, "subscribe-student-id").send_keys(std_id)
      self._driver.find_element(By.ID, "subscribe-discipline-id").click()
      disc_ID_input = self._driver.find_element(By.ID, "subscribe-discipline-id")
      disc_ID_input.clear()
      self._driver.find_element(By.ID, "subscribe-discipline-id").send_keys(disc_id)
      self._driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn").click()
 
  def get_log(self, n):
    if n is None:
      return self._driver.find_element(By.CSS_SELECTOR, ".py-p").text
    else:
      return self._driver.find_element(By.CSS_SELECTOR, f".py-p:nth-child({n})").text