for i in 1 2 3
do
  ansible-playbook /home/ubuntu/playbooks/playbook$i.yml -b
done
