
gcloud secrets create my-secret-test --replication-policy="automatic"

echo -n "Este es un texto secreto y particular" | gcloud secrets versions add my-secret-test --data-file=-

echo "Este es un texto secreto y particular 2" > my_secret_test.txt

gcloud secrets versions add my-secret-test --data-file=my_secret_test.txt

gcloud secrets versions access latest --secret=my-secret-test
