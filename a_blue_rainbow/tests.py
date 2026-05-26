from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import AssistedLivingFacility, Provider, UserFeedback


class HomePageTests(TestCase):
	def test_home_page_renders(self):
		response = self.client.get("/")

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "home-view.html")
		self.assertContains(response, "A Blue Rainbow")


class AssistedLivingViewTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.admin_user = get_user_model().objects.create_user(
			username="facility-admin",
			password="secure-pass-123",
			is_staff=True,
		)
		provider = Provider.objects.create(
			id=1,
			facility_type="Assisted Living",
			facility_name="Rainbow Provider",
		)
		cls.facility = AssistedLivingFacility.objects.create(
			facility_type=provider,
			name="Sunrise Manor",
			address="123 Main Street",
			city="Bradenton",
			state="FL",
			zip_code="34201",
		)

	def test_search_facilities_handles_missing_results(self):
		response = self.client.post("/search_facilities", {"searched": "Missing"})

		self.assertEqual(response.status_code, 200)
		self.assertIsNone(response.context["object"])

	def test_assisted_living_search_returns_match(self):
		response = self.client.get("/assistedliving/", {"q": "Sunrise"})

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["object"], self.facility)

	def test_missing_assisted_living_detail_returns_404(self):
		response = self.client.get("/assistedliving/details/999")

		self.assertEqual(response.status_code, 404)

	def test_assisted_living_create_persists_new_facility(self):
		self.client.force_login(self.admin_user)

		response = self.client.post(
			reverse("alf-create-view"),
			{
				"name": "New Horizons",
				"address": "456 Oak Avenue",
				"city": "Sarasota",
				"state": "FL",
				"zip_code": "34232",
			},
		)

		self.assertEqual(response.status_code, 302)
		self.assertTrue(response["Location"].endswith("create?submitted=True"))
		self.assertTrue(
			AssistedLivingFacility.objects.filter(name="New Horizons").exists()
		)

	def test_assisted_living_update_changes_existing_facility(self):
		self.client.force_login(self.admin_user)

		response = self.client.post(
			f"/assistedliving/update/{self.facility.pk}",
			{
				"name": "Sunrise Manor Updated",
				"address": self.facility.address,
				"city": self.facility.city,
				"state": self.facility.state,
				"zip_code": self.facility.zip_code,
			},
		)

		self.facility.refresh_from_db()
		self.assertEqual(response.status_code, 302)
		self.assertEqual(self.facility.name, "Sunrise Manor Updated")

	def test_assisted_living_delete_removes_facility(self):
		self.client.force_login(self.admin_user)

		response = self.client.get(f"/assistedliving/delete/{self.facility.pk}")

		self.assertEqual(response.status_code, 302)
		self.assertFalse(
			AssistedLivingFacility.objects.filter(pk=self.facility.pk).exists()
		)

	def test_assisted_living_create_requires_admin_login(self):
		response = self.client.get(reverse("alf-create-view"))

		self.assertEqual(response.status_code, 302)
		self.assertTrue(response["Location"].startswith("/login/?next="))


class AuthenticationViewTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.admin_user = get_user_model().objects.create_user(
			username="site-admin",
			password="secure-pass-123",
			is_staff=True,
		)

	def test_login_page_renders(self):
		response = self.client.get(reverse("login"))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Admin Sign In")

	def test_staff_user_can_log_in(self):
		response = self.client.post(
			reverse("login"),
			{"username": "site-admin", "password": "secure-pass-123"},
		)

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response["Location"], "/")


class UserFeedbackViewTests(TestCase):
	def test_feedback_page_renders(self):
		response = self.client.get("/feedback/")

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "userfeedback/feedback.html")
		self.assertContains(response, "Send Feedback")

	def test_feedback_page_post_persists_feedback(self):
		response = self.client.post(
			"/feedback/",
			{
				"name": "Jordan Rivers",
				"email": "jordan@example.com",
				"comments": "Please add more provider detail.",
			},
		)

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response["Location"], "/?submitted")
		self.assertTrue(
			UserFeedback.objects.filter(email="jordan@example.com").exists()
		)


class ApiEndpointTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.admin_user = get_user_model().objects.create_user(
			username="api-admin",
			password="secure-pass-123",
			is_staff=True,
		)
		cls.provider = Provider.objects.create(
			facility_type="Assisted Living",
			facility_name="API Provider",
		)
		cls.facility = AssistedLivingFacility.objects.create(
			facility_type=cls.provider,
			name="API Manor",
			address="789 Palm Street",
			city="Bradenton",
			state="FL",
			zip_code="34205",
		)

	def test_provider_api_list_returns_provider_data(self):
		response = self.client.get("/api/providers/")

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()[0]["facility_name"], "API Provider")

	def test_assisted_living_api_detail_returns_facility_data(self):
		response = self.client.get(f"/api/assistedliving/{self.facility.pk}/")

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()["name"], "API Manor")

	def test_feedback_api_list_returns_feedback_data(self):
		feedback = UserFeedback.objects.create(
			name="Casey Lane",
			email="casey@example.com",
			comments="Helpful directory.",
		)

		response = self.client.get("/api/feedback/")

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()[0]["id"], feedback.id)
		self.assertEqual(response.json()[0]["email"], "casey@example.com")

	def test_feedback_api_detail_returns_feedback_data(self):
		feedback = UserFeedback.objects.create(
			name="Avery Stone",
			email="avery@example.com",
			comments="Please verify addresses.",
		)

		response = self.client.get(f"/api/feedback/{feedback.pk}/")

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()["name"], "Avery Stone")

	def test_assisted_living_api_create_requires_admin_authentication(self):
		response = self.client.post(
			"/api/assistedliving/",
			{
				"facility_type": self.provider.pk,
				"name": "Locked Resource",
				"address": "100 Secure Way",
				"city": "Bradenton",
				"state": "FL",
				"zip_code": "34208",
			},
		)

		self.assertIn(response.status_code, {401, 403})

	def test_assisted_living_api_create_allows_admin_user(self):
		self.client.force_login(self.admin_user)

		response = self.client.post(
			"/api/assistedliving/",
			{
				"facility_type": self.provider.pk,
				"name": "Admin Manor",
				"address": "100 Secure Way",
				"city": "Bradenton",
				"state": "FL",
				"zip_code": "34208",
			},
		)

		self.assertEqual(response.status_code, 201)
		self.assertTrue(
			AssistedLivingFacility.objects.filter(name="Admin Manor").exists()
		)
